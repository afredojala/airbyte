/*
 * Copyright (c) 2021 Airbyte, Inc., all rights reserved.
 */

package io.airbyte.workers.temporal.scheduling.activities;

import io.airbyte.config.Configs;
import io.airbyte.config.StandardSync;
import io.airbyte.config.helpers.ScheduleHelpers;
import io.airbyte.config.persistence.ConfigNotFoundException;
import io.airbyte.config.persistence.ConfigRepository;
import io.airbyte.scheduler.models.Job;
import io.airbyte.scheduler.persistence.JobPersistence;
import io.airbyte.validation.json.JsonValidationException;
import io.airbyte.workers.temporal.exception.NonRetryableException;
import java.io.IOException;
import java.time.Duration;
import java.time.Instant;
import java.util.Optional;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@AllArgsConstructor
@Slf4j
public class ConfigFetchActivityImpl implements ConfigFetchActivity {

  private ConfigRepository configPersistence;
  private JobPersistence jobPersistence;
  private Configs configs;

  @Override
  public ScheduleRetrieverOutput getPeriodicity(final ScheduleRetrieverInput input) {
    try {
      final Optional<Job> previousJobOptional = jobPersistence.getLastReplicationJob(input.getConnectionId());
      final StandardSync standardSync = configPersistence.getStandardSync(input.getConnectionId());

      if (previousJobOptional.isEmpty()) {
        if (standardSync.getSchedule() != null) {
          // Non-manual syncs don't wait for their first run
          return new ScheduleRetrieverOutput(Duration.ZERO);
        } else {
          // Manual syncs wait for their first run
          return new ScheduleRetrieverOutput(Duration.ofDays(100 * 365));
        }
      }

      final Job previousJob = previousJobOptional.get();
      final long prevRunStart = previousJob.getStartedAtInSecond().orElse(previousJob.getCreatedAtInSecond());
      log.error("Standard sync = " + standardSync + ", schedule = " + standardSync.getSchedule());

      final long nextRunStart = prevRunStart + ScheduleHelpers.getIntervalInSecond(standardSync.getSchedule());

      final Duration timeToWait = Duration.ofSeconds(
          Math.max(0, nextRunStart - Instant.now().getEpochSecond()));

      return new ScheduleRetrieverOutput(timeToWait);
    } catch (final IOException | JsonValidationException | ConfigNotFoundException e) {
      throw new NonRetryableException(e);
    }
  }

  @Override
  public GetMaxAttemptOutput getMaxAttempt() {
    return new GetMaxAttemptOutput(configs.getSyncJobMaxAttempts());
  }

}

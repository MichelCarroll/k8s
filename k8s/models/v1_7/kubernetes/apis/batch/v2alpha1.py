#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import absolute_import

import datetime

import six

from k8s.base import Model
from k8s.fields import Field, ListField
from k8s.models.v1_7.apimachinery.apis.meta.v1 import ListMeta, ObjectMeta
from k8s.models.v1_7.kubernetes.api.v1 import ObjectReference
from k8s.models.v1_7.kubernetes.apis.batch.v1 import JobSpec


class CronJobStatus(Model):
    """
    CronJobStatus represents the current state of a cron job.
    """

    active = ListField(ObjectReference)
    lastScheduleTime = Field(datetime.datetime)


class JobTemplateSpec(Model):
    """
    JobTemplateSpec describes the data a Job should have when created from a
    template
    """

    metadata = Field(ObjectMeta)
    spec = Field(JobSpec)


class CronJobSpec(Model):
    """
    CronJobSpec describes how the job execution will look like and when it will
    actually run.
    """

    concurrencyPolicy = Field(six.text_type)
    failedJobsHistoryLimit = Field(int)
    jobTemplate = Field(JobTemplateSpec)
    schedule = Field(six.text_type)
    startingDeadlineSeconds = Field(int)
    successfulJobsHistoryLimit = Field(int)
    suspend = Field(bool)


class CronJob(Model):
    """
    CronJob represents the configuration of a single cron job.
    """
    class Meta:
        create_url = "/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs"
        delete_url = "/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}"
        get_url = "/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}"
        list_all_url = "/apis/batch/v2alpha1/cronjobs"
        list_ns_url = "/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs"
        update_url = "/apis/batch/v2alpha1/namespaces/{namespace}/cronjobs/{name}"
        watch_url = "/apis/batch/v2alpha1/watch/namespaces/{namespace}/cronjobs/{name}"
        watchlist_all_url = "/apis/batch/v2alpha1/watch/cronjobs"
        watchlist_ns_url = "/apis/batch/v2alpha1/watch/namespaces/{namespace}/cronjobs"
    
    apiVersion = Field(six.text_type, "batch/v2alpha1")
    kind = Field(six.text_type, "ScheduledJob")

    metadata = Field(ObjectMeta)
    spec = Field(CronJobSpec)
    status = Field(CronJobStatus)


class CronJobList(Model):
    """
    CronJobList is a collection of cron jobs.
    """
    apiVersion = Field(six.text_type, "batch/v2alpha1")
    kind = Field(six.text_type, "ScheduledJobList")

    items = ListField(CronJob)
    metadata = Field(ListMeta)

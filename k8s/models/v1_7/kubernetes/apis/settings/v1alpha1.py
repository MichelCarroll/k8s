#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import absolute_import

import six

from k8s.base import Model
from k8s.fields import Field, ListField
from k8s.models.v1_7.apimachinery.apis.meta.v1 import LabelSelector, ListMeta, ObjectMeta
from k8s.models.v1_7.kubernetes.api.v1 import EnvFromSource, EnvVar, Volume, VolumeMount


class PodPresetSpec(Model):
    """
    PodPresetSpec is a description of a pod preset.
    """

    env = ListField(EnvVar)
    envFrom = ListField(EnvFromSource)
    selector = Field(LabelSelector)
    volumeMounts = ListField(VolumeMount)
    volumes = ListField(Volume)


class PodPreset(Model):
    """
    PodPreset is a policy resource that defines additional runtime requirements for
    a Pod.
    """
    class Meta:
        create_url = "/apis/settings.k8s.io/v1alpha1/namespaces/{namespace}/podpresets"
        delete_url = "/apis/settings.k8s.io/v1alpha1/namespaces/{namespace}/podpresets/{name}"
        get_url = "/apis/settings.k8s.io/v1alpha1/namespaces/{namespace}/podpresets/{name}"
        list_all_url = "/apis/settings.k8s.io/v1alpha1/podpresets"
        list_ns_url = "/apis/settings.k8s.io/v1alpha1/namespaces/{namespace}/podpresets"
        update_url = "/apis/settings.k8s.io/v1alpha1/namespaces/{namespace}/podpresets/{name}"
        watch_url = "/apis/settings.k8s.io/v1alpha1/watch/namespaces/{namespace}/podpresets/{name}"
        watchlist_all_url = "/apis/settings.k8s.io/v1alpha1/watch/podpresets"
        watchlist_ns_url = "/apis/settings.k8s.io/v1alpha1/watch/namespaces/{namespace}/podpresets"
    
    apiVersion = Field(six.text_type, "settings.k8s.io/v1alpha1")
    kind = Field(six.text_type, "PodPreset")

    metadata = Field(ObjectMeta)
    spec = Field(PodPresetSpec)


class PodPresetList(Model):
    """
    PodPresetList is a list of PodPreset objects.
    """
    apiVersion = Field(six.text_type, "settings.k8s.io/v1alpha1")
    kind = Field(six.text_type, "PodPresetList")

    items = ListField(PodPreset)
    metadata = Field(ListMeta)


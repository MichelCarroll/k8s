#!/usr/bin/env python
# -*- coding: utf-8
from __future__ import absolute_import

import six

from k8s.base import Model
from k8s.fields import Field, ListField
from k8s.models.v1_7.apimachinery.apis.meta.v1 import ListMeta, ObjectMeta


class StorageClass(Model):
    """
    StorageClass describes the parameters for a class of storage for which
    PersistentVolumes can be dynamically provisioned.

    StorageClasses are non-
    namespaced; the name of the storage class according to etcd is in
    ObjectMeta.Name.
    """
    class Meta:
        create_url = "/apis/storage.k8s.io/v1/storageclasses"
        delete_url = "/apis/storage.k8s.io/v1/storageclasses/{name}"
        get_url = "/apis/storage.k8s.io/v1/storageclasses/{name}"
        list_all_url = "/apis/storage.k8s.io/v1/storageclasses"
        update_url = "/apis/storage.k8s.io/v1/storageclasses/{name}"
        watch_url = "/apis/storage.k8s.io/v1/watch/storageclasses/{name}"
        watchlist_all_url = "/apis/storage.k8s.io/v1/watch/storageclasses"
    
    apiVersion = Field(six.text_type, "storage.k8s.io/v1")
    kind = Field(six.text_type, "StorageClass")

    metadata = Field(ObjectMeta)
    parameters = Field(dict)
    provisioner = Field(six.text_type)


class StorageClassList(Model):
    """
    StorageClassList is a collection of storage classes.
    """
    apiVersion = Field(six.text_type, "storage.k8s.io/v1")
    kind = Field(six.text_type, "StorageClassList")

    items = ListField(StorageClass)
    metadata = Field(ListMeta)


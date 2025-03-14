# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/config_change.proto
"""Generated protocol buffer code."""
from cloudsdk.google.protobuf.internal import enum_type_wrapper
from cloudsdk.google.protobuf import descriptor as _descriptor
from cloudsdk.google.protobuf import message as _message
from cloudsdk.google.protobuf import reflection as _reflection
from cloudsdk.google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/api/config_change.proto",
    package="google.api",
    syntax="proto3",
    serialized_options=b"\n\016com.google.apiB\021ConfigChangeProtoP\001ZCgoogle.golang.org/genproto/googleapis/api/configchange;configchange\242\002\004GAPI",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1egoogle/api/config_change.proto\x12\ngoogle.api"\x97\x01\n\x0c\x43onfigChange\x12\x0f\n\x07\x65lement\x18\x01 \x01(\t\x12\x11\n\told_value\x18\x02 \x01(\t\x12\x11\n\tnew_value\x18\x03 \x01(\t\x12+\n\x0b\x63hange_type\x18\x04 \x01(\x0e\x32\x16.google.api.ChangeType\x12#\n\x07\x61\x64vices\x18\x05 \x03(\x0b\x32\x12.google.api.Advice"\x1d\n\x06\x41\x64vice\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t*O\n\nChangeType\x12\x1b\n\x17\x43HANGE_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x01\x12\x0b\n\x07REMOVED\x10\x02\x12\x0c\n\x08MODIFIED\x10\x03\x42q\n\x0e\x63om.google.apiB\x11\x43onfigChangeProtoP\x01ZCgoogle.golang.org/genproto/googleapis/api/configchange;configchange\xa2\x02\x04GAPIb\x06proto3',
)

_CHANGETYPE = _descriptor.EnumDescriptor(
    name="ChangeType",
    full_name="google.api.ChangeType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CHANGE_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ADDED",
            index=1,
            number=1,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="REMOVED",
            index=2,
            number=2,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="MODIFIED",
            index=3,
            number=3,
            serialized_options=None,
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=231,
    serialized_end=310,
)
_sym_db.RegisterEnumDescriptor(_CHANGETYPE)

ChangeType = enum_type_wrapper.EnumTypeWrapper(_CHANGETYPE)
CHANGE_TYPE_UNSPECIFIED = 0
ADDED = 1
REMOVED = 2
MODIFIED = 3


_CONFIGCHANGE = _descriptor.Descriptor(
    name="ConfigChange",
    full_name="google.api.ConfigChange",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="element",
            full_name="google.api.ConfigChange.element",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="old_value",
            full_name="google.api.ConfigChange.old_value",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="new_value",
            full_name="google.api.ConfigChange.new_value",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="change_type",
            full_name="google.api.ConfigChange.change_type",
            index=3,
            number=4,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="advices",
            full_name="google.api.ConfigChange.advices",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=47,
    serialized_end=198,
)


_ADVICE = _descriptor.Descriptor(
    name="Advice",
    full_name="google.api.Advice",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="description",
            full_name="google.api.Advice.description",
            index=0,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=200,
    serialized_end=229,
)

_CONFIGCHANGE.fields_by_name["change_type"].enum_type = _CHANGETYPE
_CONFIGCHANGE.fields_by_name["advices"].message_type = _ADVICE
DESCRIPTOR.message_types_by_name["ConfigChange"] = _CONFIGCHANGE
DESCRIPTOR.message_types_by_name["Advice"] = _ADVICE
DESCRIPTOR.enum_types_by_name["ChangeType"] = _CHANGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigChange = _reflection.GeneratedProtocolMessageType(
    "ConfigChange",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONFIGCHANGE,
        "__module__": "google.api.config_change_pb2"
        # @@protoc_insertion_point(class_scope:google.api.ConfigChange)
    },
)
_sym_db.RegisterMessage(ConfigChange)

Advice = _reflection.GeneratedProtocolMessageType(
    "Advice",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADVICE,
        "__module__": "google.api.config_change_pb2"
        # @@protoc_insertion_point(class_scope:google.api.Advice)
    },
)
_sym_db.RegisterMessage(Advice)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

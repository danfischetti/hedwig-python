# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf_bad1.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from hedwig import options_pb2 as hedwig_dot_options__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf_bad1.proto',
  package='tests.bad1',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13protobuf_bad1.proto\x12\ntests.bad1\x1a\x14hedwig/options.proto\"\'\n\rDeviceCreated\x12\x0e\n\x06\x66oobar\x18\x01 \x02(\x05:\x06\x9a\x82\x19\x02\x08\x01'
  ,
  dependencies=[hedwig_dot_options__pb2.DESCRIPTOR,])




_DEVICECREATED = _descriptor.Descriptor(
  name='DeviceCreated',
  full_name='tests.bad1.DeviceCreated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='foobar', full_name='tests.bad1.DeviceCreated.foobar', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\232\202\031\002\010\001',
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=96,
)

DESCRIPTOR.message_types_by_name['DeviceCreated'] = _DEVICECREATED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DeviceCreated = _reflection.GeneratedProtocolMessageType('DeviceCreated', (_message.Message,), {
  'DESCRIPTOR' : _DEVICECREATED,
  '__module__' : 'protobuf_bad1_pb2'
  # @@protoc_insertion_point(class_scope:tests.bad1.DeviceCreated)
  })
_sym_db.RegisterMessage(DeviceCreated)


_DEVICECREATED._options = None
# @@protoc_insertion_point(module_scope)
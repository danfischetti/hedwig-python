# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf_container_schema.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf_container_schema.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fprotobuf_container_schema.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa9\x01\n\nMetadataV1\x12\x11\n\tpublisher\x18\x01 \x01(\t\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x07headers\x18\x03 \x03(\x0b\x32\x18.MetadataV1.HeadersEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"l\n\tPayloadV1\x12\x16\n\x0e\x66ormat_version\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x1d\n\x08metadata\x18\x03 \x01(\x0b\x32\x0b.MetadataV1\x12\x0e\n\x06schema\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_METADATAV1_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='MetadataV1.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='MetadataV1.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='MetadataV1.HeadersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=238,
)

_METADATAV1 = _descriptor.Descriptor(
  name='MetadataV1',
  full_name='MetadataV1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='publisher', full_name='MetadataV1.publisher', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='MetadataV1.timestamp', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headers', full_name='MetadataV1.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_METADATAV1_HEADERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=238,
)


_PAYLOADV1 = _descriptor.Descriptor(
  name='PayloadV1',
  full_name='PayloadV1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='format_version', full_name='PayloadV1.format_version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='PayloadV1.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='PayloadV1.metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schema', full_name='PayloadV1.schema', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='PayloadV1.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=240,
  serialized_end=348,
)

_METADATAV1_HEADERSENTRY.containing_type = _METADATAV1
_METADATAV1.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METADATAV1.fields_by_name['headers'].message_type = _METADATAV1_HEADERSENTRY
_PAYLOADV1.fields_by_name['metadata'].message_type = _METADATAV1
DESCRIPTOR.message_types_by_name['MetadataV1'] = _METADATAV1
DESCRIPTOR.message_types_by_name['PayloadV1'] = _PAYLOADV1
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MetadataV1 = _reflection.GeneratedProtocolMessageType('MetadataV1', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _METADATAV1_HEADERSENTRY,
    '__module__' : 'protobuf_container_schema_pb2'
    # @@protoc_insertion_point(class_scope:MetadataV1.HeadersEntry)
    })
  ,
  'DESCRIPTOR' : _METADATAV1,
  '__module__' : 'protobuf_container_schema_pb2'
  # @@protoc_insertion_point(class_scope:MetadataV1)
  })
_sym_db.RegisterMessage(MetadataV1)
_sym_db.RegisterMessage(MetadataV1.HeadersEntry)

PayloadV1 = _reflection.GeneratedProtocolMessageType('PayloadV1', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADV1,
  '__module__' : 'protobuf_container_schema_pb2'
  # @@protoc_insertion_point(class_scope:PayloadV1)
  })
_sym_db.RegisterMessage(PayloadV1)


_METADATAV1_HEADERSENTRY._options = None
# @@protoc_insertion_point(module_scope)

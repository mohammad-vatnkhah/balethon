from .event_handler import EventHandler

try:
    from ..proto.updates.messaging_pb2 import Message as ProtobufMessage
except ImportError:
    class ProtobufMessage:
        pass


class RawMessageHandler(EventHandler):
    can_handle = ProtobufMessage

    async def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["message"] = event

        await super().handle(*args, **kwargs)

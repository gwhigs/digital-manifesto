from rest_framework import serializers

from .models import Annotation


class AnnotationRangeSerializer(serializers.Serializer):
    start = serializers.CharField(max_length=50, allow_blank=True)
    end = serializers.CharField(max_length=50, allow_blank=True)
    startOffset = serializers.IntegerField()
    endOffset = serializers.IntegerField()


class AnnotationSerializer(serializers.ModelSerializer):
    ranges = serializers.SerializerMethodField()

    def get_ranges(self, annot):
        ranges = [{
            'start': annot.range_start,
            'end': annot.range_end,
            'startOffset': annot.range_start_offset,
            'endOffset': annot.range_end_offset
        }]
        return ranges

    @staticmethod
    def handle_ranges(data):
        range_data = data.pop('ranges', [None])[0]
        d = {
            'range_start': range_data.get('start'),
            'range_end': range_data.get('end'),
            'range_start_offset': range_data.get('startOffset'),
            'range_end_offset': range_data.get('endOffset'),
        }
        data.update(d)
        return data

    def to_internal_value(self, data):
        """
        Annotator-js sends a `ranges` field, which is an array of mostly 1 dictionary.
        We need to unpack the fields within before sending to deserialization.
        """
        data = self.handle_ranges(data)
        return super(AnnotationSerializer, self).to_internal_value(data)

    class Meta:
        model = Annotation
        fields = (
            'id',
            'text_object',
            'annotator_schema_version',
            'text',
            'quote',
            'uri',
            'user',
            'range_start',
            'range_end',
            'range_start_offset',
            'range_end_offset',
            'ranges',
        )


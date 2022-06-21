import os

from spaceone.inventory.libs.common_parser import *
from spaceone.inventory.libs.schema.metadata.dynamic_widget import CardWidget, ChartWidget
from spaceone.inventory.libs.schema.metadata.dynamic_field import TextDyField, SearchField, DateTimeDyField, ListDyField, \
    EnumDyField, SizeField
from spaceone.inventory.libs.schema.cloud_service_type import CloudServiceTypeResource, CloudServiceTypeResponse, \
    CloudServiceTypeMeta

current_dir = os.path.abspath(os.path.dirname(__file__))

total_count_conf = os.path.join(current_dir, 'widget/total_count.yml')
count_by_region_conf = os.path.join(current_dir, 'widget/count_by_region.yml')
count_by_cluster_conf = os.path.join(current_dir, 'widget/count_by_cluster.yml')

cst_config_map = CloudServiceTypeResource()
cst_config_map.name = 'ConfigMap'
cst_config_map.provider = 'kubernetes'
cst_config_map.group = 'Config'
cst_config_map.service_code = 'ConfigMap'
cst_config_map.is_primary = True
cst_config_map.is_major = True
cst_config_map.labels = ['Application Integration', 'Container']
cst_config_map.tags = {
    'spaceone:icon': 'https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/kubernetes/config_map.svg',
}

cst_config_map._metadata = CloudServiceTypeMeta.set_meta(
    fields=[
        TextDyField.data_source('Namespace', 'data.metadata.namespace'),
        DateTimeDyField.data_source('Start Time', 'data.metadata.creation_timestamp'),
        TextDyField.data_source('Uid', 'data.uid', options={
            'is_optional': True
        })
    ],

    search=[
        SearchField.set(name='Uid', key='data.uid'),
        SearchField.set(name='Start Time', key='data.metadata.creation_timestamp')
    ],

    widget=[
        CardWidget.set(**get_data_from_yaml(total_count_conf)),
        CardWidget.set(**get_data_from_yaml(count_by_region_conf)),
        CardWidget.set(**get_data_from_yaml(count_by_cluster_conf))
    ]
)

CLOUD_SERVICE_TYPES = [
    CloudServiceTypeResponse({'resource': cst_config_map}),
]

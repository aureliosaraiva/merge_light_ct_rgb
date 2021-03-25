"""Constants for integration_blueprint."""
# Base component constants
NAME = "Integration blueprint"
DOMAIN = "integration_blueprint"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"
ISSUE_URL = "https://github.com/custom-components/integration_blueprint/issues"

DEPENDENCIES = ['light']
ICON = 'hass:lightbulb'
CURRENT_LIGHT_RGB = 'rgb'
CURRENT_LIGHT_CT = 'ct'
CONF_LIGHTS_CT = 'entity_id_light_ct'
CONF_LIGHTS_RGB = 'entity_id_light_rgb'
PLATFORM_NAME = 'merge_light_ct_rgb'

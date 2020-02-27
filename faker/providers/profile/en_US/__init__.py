from .. import Provider as ProfileProvider
import re

# Data source
#
# Area codes for states in the US.
# List of US area codes
# https://www.allareacodes.com/area_code_listings_by_state.htm
#
# Data was collected from the alphabetical listing by state


class Provider(ProfileProvider):

    def contact_info(self):
        """
        Generates a complete profile.
        If "fields" is not empty, only the fields in the list will be returned
        """
        state_abbr = self.generator.state_abbr()
        postcode = self.generator.postcode_in_state(state_abbr=state_abbr)
        street = self.generator.street_address()
        city = self.generator.city()
        phone = self.generator.phone_number()
        area_code = self.generator.area_code_in_state(state_abbr=state_abbr)

        if phone.startswith('+1'):
            phone = re.sub(r'\+1[\(\-]?\d{3}[\)\-]', area_code, phone)
        elif phone.startswith('001'):
            phone = re.sub(r'001[\-]?\d{3}[\-]', area_code, phone)
        else:
            phone = re.sub(r'[\(\-]?\d{3}[\)\-]', area_code, phone)

        return {
            'name': self.generator.name(),
            'phone': phone,
            'address': '%s %s %s %s' % (street, city, state_abbr, postcode)
        }

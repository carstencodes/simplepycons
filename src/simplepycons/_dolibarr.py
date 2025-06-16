#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class DolibarrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dolibarr"

    @property
    def original_file_name(self) -> "str":
        return "dolibarr.svg"

    @property
    def title(self) -> "str":
        return "Dolibarr"

    @property
    def primary_color(self) -> "str":
        return "#263C5C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dolibarr</title>
     <path d="M20.275 0a3.18 3.168 0 0 0-3.18 3.169 3.18 3.168 0 0 0
 3.18 3.168 3.18 3.168 0 0 0 3.18-3.168A3.18 3.168 0 0 0 20.275
 0ZM.545.353v23.645H7.63L7.64 7.104h2.395c4.066 0 6.099 1.602 6.099
 4.806 0 3.41-2.068 5.115-6.204 5.115H8.794v6.97s1.683.005
 2.114.005c3.67 0 6.67-1.125 9-3.376 2.33-2.25 3.495-5.155 3.495-8.714
 0-2.072-.423-3.903-1.268-5.493a3.803 3.803 0 0 1-1.86.495c-.982
 0-1.96-.403-2.654-1.096a3.782 3.782 0 0
 1-1.1-2.647c0-.533.12-1.063.34-1.548C14.913.776 12.557.353 9.79.353Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Dolibarr/dolibarr-foundati
on/blob/39f562651f88c4c4a4cd5754c18a7a2cd3dd5e59/logo-cliparts/dolibar'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []

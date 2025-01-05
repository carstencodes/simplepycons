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


class FugaCloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fugacloud"

    @property
    def original_file_name(self) -> "str":
        return "fugacloud.svg"

    @property
    def title(self) -> "str":
        return "Fuga Cloud"

    @property
    def primary_color(self) -> "str":
        return "#242F4B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fuga Cloud</title>
     <path d="m19.0876 13.9765-1.1014-.6361v-2.5345l1.1013.6389
 3.1738-1.8305v2.5275zm-14.1752.01h-.0067l-3.167-1.8341V9.625l3.1702
 1.8284 1.0982-.6371v2.5345zm.0592-3.5472L1.7387
 8.5686V5.9464l.971-.5568L11.9941 0l1.9539 1.1371 5.9567
 3.4708.2013.1303 1.0303.5922.1657.095.9593.5686v2.5597l-3.1738
 1.8349-1.1013-.6353V8.4341l-4.95-2.8903-1.0421-.6277-.971.5567-5.033
 2.9495v1.4254l-1.0185.5883m0 4.4197 1.0184-.5805v1.2082l6.0633
 3.5418.225-.1421.0473-.024
 5.6725-3.3168-.0119-.4264v-.8918l1.1014.6313
 3.1737-1.833v5.0193l-.9593.5568-1.196.6988-.2013.1185-5.9567
 3.4826L11.994
 24l-1.9302-1.1371-5.9685-3.4708-.2013-.1303-1.1842-.687-.9711-.5698v-4.6197l.0118-.3971
 3.2211 1.8673" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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

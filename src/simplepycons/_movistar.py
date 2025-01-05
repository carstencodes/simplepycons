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


class MovistarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "movistar"

    @property
    def original_file_name(self) -> "str":
        return "movistar.svg"

    @property
    def title(self) -> "str":
        return "Movistar"

    @property
    def primary_color(self) -> "str":
        return "#019DF4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Movistar</title>
     <path d="M4.512 5.187c-1.113.018-3.165.567-4.102 4.401-.409
 1.67-.567 3.413-.217 5.485.322 1.912.893 3.562 1.278
 4.471.132.314.339.64.498.842.456.579 1.217.542
 1.536.384.348-.172.748-.586.605-1.534-.07-.458-.272-1.127-.386-1.499-.349-1.141-.814-2.518-.854-3.5-.054-1.311.463-1.483.806-1.56.576-.126
 1.06.508 1.52 1.303.548.949 1.488 2.63 2.255 3.915.692 1.16 1.97
 2.401 4.02 2.316 2.091-.087 3.633-.886
 4.427-3.402.594-1.882.999-3.289 1.651-4.729.75-1.657 1.75-2.543
 2.592-2.272.782.25.977 1.016.986 2.14.009.996-.107 2.093-.196
 2.898-.032.293-.09.881-.066 1.207.047.643.325 1.284 1.046
 1.386.77.109 1.387-.506
 1.633-1.25.098-.293.18-.742.225-1.06.226-1.608.284-2.689.183-4.333-.12-1.924-.495-3.678-1.152-5.196-.627-1.452-1.635-2.382-2.927-2.464-1.43-.091-3.072.86-3.934
 2.704-.793 1.7-1.428 3.444-1.814 4.336-.39.903-.965 1.459-1.847
 1.552-1.08.114-2.01-.67-2.692-1.79-.593-.975-1.77-2.832-2.4-3.456-.592-.584-1.267-1.317-2.674-1.295z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://brandfactory.telefonica.com/document/'''
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

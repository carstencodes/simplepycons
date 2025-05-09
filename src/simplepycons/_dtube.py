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


class DtubeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dtube"

    @property
    def original_file_name(self) -> "str":
        return "dtube.svg"

    @property
    def title(self) -> "str":
        return "DTube"

    @property
    def primary_color(self) -> "str":
        return "#F01A30"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DTube</title>
     <path d="M0 1.6416v20.7168h8.5156c1.3133 0 2.4886-.1588
 3.5371-.4766 1.038-.3177 1.9716-.7833 2.7871-1.4082 1.1545-.8896
 2.0431-2.0456
 2.668-3.4648.6143-1.4192.9316-3.0486.9316-4.8809-.0105-1.578-.243-3.0203-.709-4.3125-.466-1.2921-1.1116-2.3919-1.959-3.3027-.8366-.9109-1.8536-1.6108-3.0292-2.1191-1.1757-.4979-2.4784-.752-3.9082-.752zm5.2012
 5.709l8.039 4.6601-8.039 4.6485zm15.9922 9.162c-1.4934 0-2.711
 1.2177-2.711 2.711 0 1.4934 1.2176 2.711 2.711 2.711h.0957c1.4933 0
 2.7109-1.2176 2.7109-2.711 0-1.4933-1.2176-2.711-2.711-2.711z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/dtube/about/blob/bb688ac65'''

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

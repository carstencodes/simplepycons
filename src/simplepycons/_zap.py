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


class ZapIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zap"

    @property
    def original_file_name(self) -> "str":
        return "zap.svg"

    @property
    def title(self) -> "str":
        return "ZAP"

    @property
    def primary_color(self) -> "str":
        return "#00549E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ZAP</title>
     <path d="M15.1449 14.1032a.17.17 0 0 1
 .0865-.2689l1.7154-.4203c.1261-.0367.1364-.1735.1236-.2288a.1655.1655
 0 0 0-.0216-.0401L13.071
 8.1627c-.0727-.102-.0294-.2272.0741-.2658l1.3445-.4327a.1669.1669 0 0
 0 .0804-.2565L9.5568.0804a.1545.1545 0 0 0-.1886-.068L.099
 4.0304a.17.17 0 0 0-.0309.2905l5.1678 3.6718a.1607.1607 0 0 1
 .068.1515c-.0015.063-.0488.1081-.0557.1144l-.0402.0247-1.2146.5316a.17.17
 0 0 0-.0897.0958v.0402a.1824.1824 0 0 0 .068.1545c1.7749 1.281 3.5502
 2.5614 5.3254
 3.8418.109.0844.0741.243-.0402.2937l-1.5793.6181c-.1282.054-.1401.2298-.0217.2998l13.1142
 7.5724c.1507.0627.2904-.1097.1978-.2442l-5.823-7.3838zm.1483-7.4024a1.0694
 1.0694 0 0 1 .136.9272 1.0447 1.0447 0 0 1-.6676.6615l-.3616.1174
 3.3195 4.191a1.0478 1.0478 0 0 1-.5656 1.6722l-.6182.1545 4.4816
 5.6778A11.677 11.677 0 0 0 12.3168.6305c-.4142
 0-.8221.0217-1.2363.0619zM7.211 14.9284a1.0509 1.0509 0 0 1
 .139-1.8822l.3771-.1453L3.4587 9.81a1.0509 1.0509 0 0 1
 .1916-1.8112l.0618-.0278-1.6906-1.1868a11.68 11.68 0 0 0 17.098
 15.021Z" />
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
        yield from [
            "Zed Attack Proxy",
        ]

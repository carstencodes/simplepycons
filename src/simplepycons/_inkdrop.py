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


class InkdropIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "inkdrop"

    @property
    def original_file_name(self) -> "str":
        return "inkdrop.svg"

    @property
    def title(self) -> "str":
        return "Inkdrop"

    @property
    def primary_color(self) -> "str":
        return "#7A78D7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Inkdrop</title>
     <path d="M8.8538 1.8124C9.423.8338 10.471.1434
 11.607.0204c.9389-.1016 1.9145.1801 2.6558.7704a3.665 3.665 0 0 1
 .873 1.0085c2.1647 3.7212 4.314 7.4514 6.471 11.1772.3424.5943.5005
 1.282.4751 1.9621-.0216.5791-.1762 1.1527-.4632 1.6586-1.067
 1.8622-2.1418 3.72-3.2127 5.58-.6375 1.1018-1.868 1.8129-3.134
 1.8209-2.1693.0043-4.3387 0-6.508
 0-1.2684-.0027-2.4975-.711-3.1373-1.8003-1.0817-1.8593-2.1556-3.7232-3.2335-5.585-.6362-1.1042-.6358-2.5271-.0076-3.6282
 2.1483-3.7285 4.312-7.4481 6.468-11.1721ZM4.625 14.1495a1.1916 1.1916
 0 0 0 0 1.183c1.074 1.864 2.085 3.6278 3.1744 5.4828a1.1875 1.1875 0
 0 0 1.019.5845c2.1693.0046 4.2194.0135 6.3887 0a1.1873 1.1873 0 0 0
 1.0179-.5912c1.0746-1.858 2.0949-3.6112 3.154-5.4781a1.1876 1.1876 0
 0
 0-.004-1.176c-2.1496-3.73-4.1723-7.26-6.3524-10.9724-.2298-.3875-.666-.6167-1.1181-.5809a1.1856
 1.1856 0 0 0-.9324.5853 2974.9829 2974.9829 0 0 0-6.347
 10.963Zm8.4659 4.0637a1.2598 1.2598 0 0 1-2.182 0L8.745 14.465a1.2597
 1.2597 0 0 1 1.091-1.8896h4.328a1.2597 1.2597 0 0 1 1.091
 1.8896l-2.164 3.7481Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://site-cdn.inkdrop.app/site/icons/inkdr'''

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

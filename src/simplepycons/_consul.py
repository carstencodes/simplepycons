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


class ConsulIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "consul"

    @property
    def original_file_name(self) -> "str":
        return "consul.svg"

    @property
    def title(self) -> "str":
        return "Consul"

    @property
    def primary_color(self) -> "str":
        return "#F24C53"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Consul</title>
     <path d="M14.0754 12.0285a2.5059 2.5059 0 0 0-2.506-2.506 2.5059
 2.5059 0 0 0-2.5058 2.506 2.5059 2.5059 0 0 0 2.5059 2.5059 2.5059
 2.5059 0 0 0 2.5059-2.506zm3.5317.0003a1.1559 1.1556 0 0
 0-1.1558-1.1556 1.1559 1.1556 0 0 0-1.1559 1.1556 1.1559 1.1556 0 0 0
 1.1559 1.1555 1.1559 1.1556 0 0 0 1.1558-1.1555zm4.7917 5.5103a1.1576
 1.1564 0 0 0-1.1577-1.1564 1.1576 1.1564 0 0 0-1.1576 1.1564 1.1576
 1.1564 0 0 0 1.1576 1.1564 1.1576 1.1564 0 0 0 1.1577-1.1564zM20.748
 13.888a1.1534 1.157 0 0 0-1.1533-1.157 1.1534 1.157 0 0 0-1.1534
 1.157 1.1534 1.157 0 0 0 1.1534 1.1571 1.1534 1.157 0 0 0
 1.1533-1.157zm3.2512.0619a1.1542 1.1538 0 0 0-1.1542-1.1538 1.1542
 1.1538 0 0 0-1.1542 1.1538 1.1542 1.1538 0 0 0 1.1542 1.1538 1.1542
 1.1538 0 0 0 1.1542-1.1538zm-3.279-3.883a1.1561 1.1535 0 0
 0-1.156-1.1535 1.1561 1.1535 0 0 0-1.1562 1.1535 1.1561 1.1535 0 0 0
 1.1561 1.1535 1.1561 1.1535 0 0 0 1.1562-1.1535zm3.2798.045a1.1614
 1.157 0 0 0-1.1614-1.157 1.1614 1.157 0 0 0-1.1613 1.157 1.1614 1.157
 0 0 0 1.1613 1.1572A1.1614 1.157 0 0 0 24
 10.1119zm-1.626-3.631a1.1575 1.1601 0 0 0-1.1575-1.16 1.1575 1.1601 0
 0 0-1.1575 1.16 1.1575 1.1601 0 0 0 1.1575 1.1602A1.1575 1.1601 0 0 0
 22.374 6.481zM11.6171.3832c-3.1098 0-6.029 1.2063-8.2197 3.3974C1.206
 5.9822 0 8.9007 0 11.9998c0 3.109 1.2067 6.0279 3.3974 8.2193 2.2028
 2.1922 5.1213 3.3978 8.2197 3.3978 2.578 0 5.0176-.8252
 7.055-2.386l-1.4196-1.8524c-1.6263 1.246-3.5748 1.9048-5.6354
 1.9048-2.4776
 0-4.8112-.9641-6.5717-2.7154-1.748-1.7488-2.7118-4.0828-2.7118-6.568
 0-2.4784.9645-4.812 2.7158-6.5703 1.7484-1.7488 4.0817-2.713
 6.5677-2.713 2.058 0 4.0069.659 5.6365 1.9057l1.4179-1.854C16.6314
 1.2083 14.1922.3831 11.617.3831Z" />
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

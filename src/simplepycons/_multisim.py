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


class MultisimIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "multisim"

    @property
    def original_file_name(self) -> "str":
        return "multisim.svg"

    @property
    def title(self) -> "str":
        return "Multisim"

    @property
    def primary_color(self) -> "str":
        return "#57B685"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Multisim</title>
     <path d="M20.3636 5.7778c-.1616.3232-.5656.5656-.9697.5656-.6464
 0-1.1313-.4848-1.1313-1.1313s.4849-1.1313 1.1313-1.1313c.404 0
 .7273.2424.9697.5657h3.5556V.1212H0v2.7475h15.0303c.1616-.3232.5657-.5657.9697-.5657.6465
 0 1.1313.4849 1.1313 1.1313S16.6465 4.5657 16 4.5657c-.404
 0-.7273-.2425-.9697-.5657H0v6.5455h2.101V6.505h10.586c.1616-.3232.5656-.5656.9697-.5656.6464
 0 1.1313.4848 1.1313 1.1313s-.485 1.1313-1.1314 1.1313c-.404
 0-.7273-.2424-.9697-.5656H3.313v3.0707h11.798c.1616-.3233.5657-.5657.9697-.5657.6465
 0 1.1313.4849 1.1313 1.1313s-.4848 1.1313-1.1313 1.1313c-.404
 0-.7273-.2424-.9697-.5656H0v3.0707h6.5455c.1616-.3232.5656-.5657.9697-.5657.6464
 0 1.1313.4849 1.1313 1.1313 0 .6465-.4849 1.1314-1.1313 1.1314-.404
 0-.7273-.2425-.9697-.5657H0v3.0707h7.6768c.1616-.3232.5656-.5657.9697-.5657.6464
 0 1.1313.4849 1.1313 1.1314 0 .6464-.4849 1.1313-1.1313 1.1313-.404
 0-.7273-.2424-.9697-.5657H0v3.6364h12.606v-7.4344c-.3232-.1616-.5656-.5656-.5656-.9697
 0-.6464.4849-1.1313 1.1313-1.1313s1.1313.4849 1.1313 1.1313c0
 .404-.2424.7273-.5656.9697v7.4344h2.6666v-5.6566c-.3232-.1616-.5656-.5656-.5656-.9697
 0-.6464.4848-1.1313 1.1313-1.1313s1.1313.4849 1.1313 1.1313c0
 .404-.2424.7273-.5656.9697v5.6566h2.6666v-8.3232c-.3232-.1617-.5656-.5657-.5656-.9697
 0-.6465.4848-1.1314 1.1313-1.1314.6464 0 1.1313.4849 1.1313 1.1314 0
 .404-.2424.7272-.5657.9697v8.3232H24V9.9798h-2.9899c-.1616.3232-.5657.5657-.9697.5657-.6465
 0-1.1313-.4849-1.1313-1.1314s.4848-1.1313 1.1313-1.1313c.404 0
 .7273.2425.9697.5657H24V5.697l-3.6364.0808z" />
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

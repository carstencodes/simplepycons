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


class AlipayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alipay"

    @property
    def original_file_name(self) -> "str":
        return "alipay.svg"

    @property
    def title(self) -> "str":
        return "Alipay"

    @property
    def primary_color(self) -> "str":
        return "#1677FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Alipay</title>
     <path d="M19.695 15.07c3.426 1.158 4.203 1.22 4.203
 1.22V3.846c0-2.124-1.705-3.845-3.81-3.845H3.914C1.808.001.102
 1.722.102 3.846v16.31c0 2.123 1.706 3.845 3.813 3.845h16.173c2.105 0
 3.81-1.722 3.81-3.845v-.157s-6.19-2.602-9.315-4.119c-2.096 2.602-4.8
 4.181-7.607 4.181-4.75 0-6.361-4.19-4.112-6.949.49-.602 1.324-1.175
 2.617-1.497 2.025-.502 5.247.313 8.266 1.317a16.796 16.796 0 0 0
 1.341-3.302H5.781v-.952h4.799V6.975H4.77v-.953h5.81V3.591s0-.409.411-.409h2.347v2.84h5.744v.951h-5.744v1.704h4.69a19.453
 19.453 0 0 1-1.986 5.06c1.424.52 2.702 1.011 3.654
 1.333m-13.81-2.032c-.596.06-1.71.325-2.321.869-1.83 1.608-.735 4.55
 2.968 4.55 2.151 0 4.301-1.388
 5.99-3.61-2.403-1.182-4.438-2.028-6.637-1.809" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://global.alipay.com/docs/ac/website_hk/'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://global.alipay.com/docs/ac/website_hk/'''

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

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


class SparkasseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sparkasse"

    @property
    def original_file_name(self) -> "str":
        return "sparkasse.svg"

    @property
    def title(self) -> "str":
        return "Sparkasse"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sparkasse</title>
     <path d="M7.0602 12.3061v1.8455h14.175v6.7773c.0296 1.6615-1.4064
 3.1066-3.0705
 3.0705H5.8352c-1.6582.0306-3.1011-1.4121-3.0705-3.0705v-1.225H16.908v-1.8455H2.7648v-6.7773c-.0307-1.6579
 1.4123-3.1012 3.0704-3.0704h12.3295c1.6641-.0363 3.1 1.4095 3.0705
 3.0705v1.225H7.0602zm4.9241-6.1486c1.7003 0 3.0787-1.3784
 3.0787-3.0787S13.6847 0 11.9843 0 8.9055 1.3784 8.9055 3.0788s1.3785
 3.0787 3.0788 3.0787z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.sparkasse.de/nutzungshinweise.htm'''
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

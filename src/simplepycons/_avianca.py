#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class AviancaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "avianca"

    @property
    def original_file_name(self) -> "str":
        return "avianca.svg"

    @property
    def title(self) -> "str":
        return "avianca"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>avianca</title>
     <path d="M3.813 0s-2.326 2.052-2.51 6.367c-.205 4.716 2.324 9.47
 10.654 10.076.026.005.055.005.08.008C7.806 11.534 4.955 5.241 3.812
 0zm8.224 16.451a30.654 30.654 0 0 0 2.2 2.303H5.282c.12.278.53.472
 1.463.527 5.59.332 6.38 4.719 14.381 4.719.702 0 1.14-.042
 1.582-.125-3.16-.972-6-2.8-8.47-5.121h2.21c.917 0 1.325.076
 1.58.191-.392-1.218-1.631-2.168-5.992-2.494z" />
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
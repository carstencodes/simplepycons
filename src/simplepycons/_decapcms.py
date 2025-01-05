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


class DecapCmsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "decapcms"

    @property
    def original_file_name(self) -> "str":
        return "decapcms.svg"

    @property
    def title(self) -> "str":
        return "Decap CMS"

    @property
    def primary_color(self) -> "str":
        return "#FF0082"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Decap CMS</title>
     <path d="M18.947 13.177c0 3.263-2 5.649-4.736
 5.649h-2.773v-5.65H6.282v10.387h7.93c5.403 0 9.788-4.668
 9.788-10.386h-5.052ZM7.894.476 0 1.212l.948 10.352
 5.157-.456-.526-5.615 2.737-.245c2.737-.246 4.91 1.93 5.227
 5.193l5.052-.458c-.49-5.752-5.297-9.998-10.7-9.507Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/decaporg/decap-cms/blob/ba
158f4a56d6d79869811971bc1bb0ef15197d30/website/static/img/decap-logo.s'''

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

#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class IndiewebIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "indieweb"

    @property
    def original_file_name(self) -> "str":
        return "indieweb.svg"

    @property
    def title(self) -> "str":
        return "IndieWeb"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>IndieWeb</title>
     <path d="M20.387 8.258A3.643 3.643 0 0 1 24 11.54h-3.613a.35.35 0
 0 0-.348.348c.009.182.13.32.312.346l.036.002H24c-.178 1.872-1.75
 3.258-3.613 3.282a3.63 3.63 0 1 1 0-7.26m-9.938.247 3.359 7.237
 3.39-7.237zm-2.941 0 3.359 7.237 1.099-2.283-2.338-4.954zM0
 11.083h6.78v4.125H0zm0-2.578h6.78v1.897H0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://indieweb.org/images/d/d4/IWC_Vector.s'''

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

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


class ValveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "valve"

    @property
    def original_file_name(self) -> "str":
        return "valve.svg"

    @property
    def title(self) -> "str":
        return "Valve"

    @property
    def primary_color(self) -> "str":
        return "#F74843"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Valve</title>
     <path d="M0 8.579v6.842h24V8.58zm1.8 1.415h.793l.776
 3.044.76-3.044h.836l-1.227 4.029H3zm5.488 0h1.084l1.145
 4.034h-.814l-.27-1.007H7.228s-.21.81-.254.99c-.242.017-.83 0-.83
 0zm4.184 0h.792v3.352h1.69v.677h-2.482zm3.45 0h.816l.776
 3.005.754-3.005h.815l-1.222 4.034h-.716zm4.828
 0h1.69v.522h-1.084v.584h.99v.523h-.99v.6h1.084v.523h-1.69zm-11.902.68l-.426
 1.702h.89z" />
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

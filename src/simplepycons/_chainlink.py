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


class ChainlinkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chainlink"

    @property
    def original_file_name(self) -> "str":
        return "chainlink.svg"

    @property
    def title(self) -> "str":
        return "Chainlink"

    @property
    def primary_color(self) -> "str":
        return "#375BD2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Chainlink</title>
     <path d="M12 0L9.798 1.266l-6 3.468L1.596 6v12l2.202 1.266 6.055
 3.468L12.055 24l2.202-1.266 5.945-3.468L22.404
 18V6l-2.202-1.266-6-3.468zM6 15.468V8.532l6-3.468 6 3.468v6.936l-6
 3.468z" />
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

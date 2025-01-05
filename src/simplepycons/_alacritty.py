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


class AlacrittyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "alacritty"

    @property
    def original_file_name(self) -> "str":
        return "alacritty.svg"

    @property
    def title(self) -> "str":
        return "Alacritty"

    @property
    def primary_color(self) -> "str":
        return "#F46D01"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Alacritty</title>
     <path d="m10.065 0-8.57 21.269h3.595l6.91-16.244 6.91
 16.244h3.594l-8.57-21.269zm1.935 9.935c-0.76666 1.8547-1.5334
 3.7094-2.298 5.565 1.475 4.54 1.475 4.54 2.298 8.5 0.823-3.96
 0.823-3.96 2.297-8.5-0.76637-1.8547-1.5315-3.7099-2.297-5.565z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/alacritty/alacritty/blob/6
d8db6b9dfadd6164c4be7a053f25db8ef6b7998/extra/logo/alacritty-simple.sv'''

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

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


class SketchIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sketch"

    @property
    def original_file_name(self) -> "str":
        return "sketch.svg"

    @property
    def title(self) -> "str":
        return "Sketch"

    @property
    def primary_color(self) -> "str":
        return "#F7B500"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sketch</title>
     <path d="M12 1.25l6.75 6.637V2L12 1.25zm0 0l-6.05
 7h12.1l-6.05-7zm0 0L5.25 2v5.887L12 1.25zM5.25 2L0 9l4.416-.68L5.25
 2zM0 9l11.959 13.703.008-.014L4.443 9H0zm18.75-7l.834 6.32L24
 9l-5.25-7zM24 9h-4.506l-7.523 13.69.029.06L24 9zM12
 22.75l-.031-.057-.008.012.039.045zM5.436 9l6.533 13.686L18.564
 9H5.436Z" />
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

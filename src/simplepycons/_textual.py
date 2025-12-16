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


class TextualIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "textual"

    @property
    def original_file_name(self) -> "str":
        return "textual.svg"

    @property
    def title(self) -> "str":
        return "Textual"

    @property
    def primary_color(self) -> "str":
        return "#FFFFFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Textual</title>
     <path d="M13.746 2.731H24l-1.722 3.873-3.143 1.768H17l-5.182
 10.552-3.128 2.345H5.283l.747-11.216H1.67L0
 6.296l2.511-1.884h8.246zM2.709 5.006l-1.45
 1.088h8.952l.249-1.088zM.825 6.69l1.23 2.77h4.611l-.747
 11.215h.941L10.074 6.69zm7.567 13.985
 5.232-12.897h5.24l1.23-2.77H11.07L7.469
 20.675zm14.02-17.35h-8.508l-1.935 1.087h8.505z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Textualize/textual/blob/e6
6c098588360515864ce88982de494c64d2c097/docs/images/icons/logo%20light%'''

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

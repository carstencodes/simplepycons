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


class AutoitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "autoit"

    @property
    def original_file_name(self) -> "str":
        return "autoit.svg"

    @property
    def title(self) -> "str":
        return "AutoIt"

    @property
    def primary_color(self) -> "str":
        return "#5D83AC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AutoIt</title>
     <path d="m19.351 15.563-5.486-7.941a2.684 2.684 0 0
 0-.702-.702c-.276-.188-.62-.283-1.03-.283-.43
 0-.784.101-1.064.302-.28.202-.512.43-.696.683l-5.63
 7.94h3.215l4.122-5.827 1.575
 2.323c.148.21.304.436.466.676.161.24.304.44.426.597a9.106 9.106 0 0
 0-.741-.026H10.78l-1.64 2.258zM12 24C5.373 24 0 18.627 0 12S5.373 0
 12 0s12 5.373 12 12-5.373 12-12 12zm0-21.61a9.61 9.61 0 1 0 0 19.22
 9.61 9.61 0 1 0 0-19.22z" />
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

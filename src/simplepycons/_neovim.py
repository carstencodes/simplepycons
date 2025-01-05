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


class NeovimIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "neovim"

    @property
    def original_file_name(self) -> "str":
        return "neovim.svg"

    @property
    def title(self) -> "str":
        return "Neovim"

    @property
    def primary_color(self) -> "str":
        return "#57A143"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Neovim</title>
     <path d="M2.214 4.954v13.615L7.655 24V10.314L3.312 3.845 2.214
 4.954zm4.999 17.98l-4.557-4.548V5.136l.59-.596 3.967
 5.908v12.485zm14.573-4.457l-.862.937-4.24-6.376V0l5.068 5.092.034
 13.385zM7.431.001l12.998 19.835-3.637 3.637L3.787 3.683 7.43 0z" />
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

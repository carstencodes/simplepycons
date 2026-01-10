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


class PixabayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pixabay"

    @property
    def original_file_name(self) -> "str":
        return "pixabay.svg"

    @property
    def title(self) -> "str":
        return "Pixabay"

    @property
    def primary_color(self) -> "str":
        return "#191B26"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pixabay</title>
     <path d="M2 0a2 2 0 0 0-2 2v20a2 2 0 0 0 2 2h20a2 2 0 0 0 2-2V2a2
 2 0 0 0-2-2Zm10.193 5.5h2.499l1.967 2.872L18.854 5.5h2.482l-3.579
 4.592 3.91 4.813h-2.638l-2.395-3.064-2.15
 3.064h-2.579l3.579-4.813zm-5.045.004c1.32.033 2.42.49 3.3
 1.371.879.881 1.335 1.986 1.37 3.317-.035 1.331-.491 2.441-1.37
 3.328-.88.887-1.98 1.346-3.3
 1.38H4.346v3.768H2.5v-8.476c.032-1.33.486-2.436 1.359-3.317.873-.88
 1.97-1.338 3.29-1.37Zm0
 1.864c-.797.02-1.46.294-1.985.823-.525.53-.797 1.196-.817
 2v2.847h2.802c.808-.019 1.476-.294
 2.003-.826.528-.532.8-1.206.82-2.02-.02-.805-.292-1.47-.82-2-.527-.53-1.195-.805-2.003-.824Z"
 />
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

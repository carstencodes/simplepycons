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


class BFourXIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "b4x"

    @property
    def original_file_name(self) -> "str":
        return "b4x.svg"

    @property
    def title(self) -> "str":
        return "B4X"

    @property
    def primary_color(self) -> "str":
        return "#14AECB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>B4X</title>
     <path d="M14.538 23.992c-6.265-.455-10.82-3-13.57-7.574a13 13 0 0
 1-.814-1.575c0-.09 7.728-14.238 7.76-14.22a2 2 0 0 1
 .068.46c.075.925.373 2.335.71 3.357a14.8 14.8 0 0 0 2.044 3.97 4 4 0
 0 0
 .37.456c.033.022.22.227.417.462.198.235.49.553.653.71l.299.283-.325-.355a19
 19 0 0 1-.597-.697l-.276-.34.478-.843
 3.835-6.769c.418-.735.769-1.328.776-1.317a8 8 0 0 1-.126.746c-.665
 3.291-.5 6.258.477 8.728.164.418.523 1.157.56 1.157.015 0
 .26-.433.545-.96a1795 1795 0 0 1 4.13-7.593 1 1 0 0 1 .13-.201c.012
 0-.066.239-.17.53-.575 1.593-.945 3.097-1.135 4.627-.093.746-.082
 2.492.026 3.194.287 1.899.95 3.455 2.026
 4.735.362.429.787.828.952.888.048.018.074.06.063.09l-1.683 3.79A284
 284 0 0 0 20.5 23.5c0
 .09-.168.142-.735.235-1.16.186-1.948.242-3.478.261-.82.008-1.604.004-1.75-.007"
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
        return '''https://www.b4x.com/android/forum/threads/b4x'''

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

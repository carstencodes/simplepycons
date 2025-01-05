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


class SanityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sanity"

    @property
    def original_file_name(self) -> "str":
        return "sanity.svg"

    @property
    def title(self) -> "str":
        return "Sanity"

    @property
    def primary_color(self) -> "str":
        return "#F03E2F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sanity</title>
     <path d="M7.394 7.31a5.745 5.745 0 0
 1-.833-.68c-.913-.91-1.38-2.067-1.38-3.568v-.575C6.699.929 9.039 0
 11.828 0c5.394 0 8.515 2.8 9.285
 6.74H16.22c-.54-1.554-1.89-2.764-4.352-2.764-2.422 0-4.136
 1.276-4.473 3.334h-.002ZM4.683 3.062c0 3.236 2.034 5.162 6.106
 6.177l4.316.983c3.854.87 6.2 3.03 6.2 6.55a6.61 6.61 0 0 1-1.436
 4.239c0-3.511-1.85-5.409-6.31-6.55l-4.236-.946c-3.393-.76-6.011-2.536-6.011-6.36a6.578
 6.578 0 0 1 1.37-4.093ZM17.18 16.484c-.292 2.235-2.092 3.495-4.698
 3.495-2.314 0-4.048-.946-4.703-2.99H2.694C3.518 21.44 7.224 24 12.519
 24c2.828 0 5.277-.87
 6.85-2.439v-.55c0-1.66-.433-2.876-1.342-3.816a5.508 5.508 0 0
 0-.847-.71v-.001Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/sanity-io/logos/blob/6934d'''

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

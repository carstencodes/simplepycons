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


class DgraphIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dgraph"

    @property
    def original_file_name(self) -> "str":
        return "dgraph.svg"

    @property
    def title(self) -> "str":
        return "Dgraph"

    @property
    def primary_color(self) -> "str":
        return "#E50695"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dgraph</title>
     <path d="M18.22 4.319c.226-.414.349-.892.349-1.403A2.917 2.917 0
 0015.653 0c-1.37 0-2.522.944-2.838
 2.218-.272-.013-.544-.033-.815-.033-5.58 0-10.1 4.513-10.1 10.1 0
 2.74 1.1 5.23 2.871 7.047a2.916 2.916 0 00-.588 1.752A2.917 2.917 0
 007.1 24c1.241 0 2.295-.782 2.728-1.869a10.092 10.092 0 0012.272-9.86
 9.982 9.982 0 00-3.88-7.952zm-2.554.381c-.162
 0-.304-.013-.446-.064l-1.21 3.523 1.772-.284-2.489 4.067
 2.075-.511-7.002 8.34c.35.317.556.783.556 1.307a1.78 1.78 0 01-1.784
 1.784c-.99 0-1.785-.795-1.785-1.784s.796-1.785 1.785-1.785c.226 0
 .446.045.653.13l1.978-4.326-1.933.524 3.142-4.5-1.933.465L14.521
 4.3c-.4-.337-.64-.828-.64-1.371 0-.99.796-1.785 1.785-1.785s1.784.796
 1.784 1.785c.007.97-.795 1.771-1.784 1.771z" />
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

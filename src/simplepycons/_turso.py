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


class TursoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "turso"

    @property
    def original_file_name(self) -> "str":
        return "turso.svg"

    @property
    def title(self) -> "str":
        return "Turso"

    @property
    def primary_color(self) -> "str":
        return "#4FF8D2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Turso</title>
     <path d="m23.31.803-.563-.42-1.11 1.189-.891-1.286-.512.235.704
 1.798-.326.35L18.082 0l-.574.284 2.25
 4.836-2.108.741h-.05l-1.143-1.359-1.144 1.36H8.687l-1.144-1.36-1.146
 1.363H6.36l-2.12-.745L6.491.284 5.919 0l-2.53
 2.668-.327-.349.705-1.798-.512-.236-.89 1.287L1.253.382.69.804 2.42
 3.69l-.89.939.311 2.375 2.061.787L3.9 8.817H1.947v.444l.755 1.078
 1.197.433v6.971l3.057 4.55L7.657 24l1.101-1.606L9.9 24l.999-1.606L12
 24l1.102-1.606L14.1 24l1.141-1.606L16.343 24l.701-1.706
 3.058-4.55v-6.972l1.196-.433.756-1.078v-.444h-1.952l.003-1.03
 2.054-.784.311-2.375-.89-.939zm-8.93 18.718H8.033l.793-1.615.794
 1.615.793-1.083.793 1.083.794-1.083.793 1.083.794-1.083.793
 1.083.793-1.615.794 1.615zm3.886-7.39-3.3 1.084-.143
 3.061-2.827.627-2.826-.627-.142-3.06-3.3-1.085v-1.635l4.266 1.21-.052
 4.126h4.109l-.052-4.127 4.266-1.209z" />
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

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


class IonicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ionic"

    @property
    def original_file_name(self) -> "str":
        return "ionic.svg"

    @property
    def title(self) -> "str":
        return "Ionic"

    @property
    def primary_color(self) -> "str":
        return "#3880FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ionic</title>
     <path d="M22.922 7.027l-.103-.23-.169.188c-.408.464-.928.82-1.505
 1.036l-.159.061.066.155a9.745 9.745 0 0 1 .75 3.759c0 5.405-4.397
 9.806-9.806 9.806-5.409 0-9.802-4.397-9.802-9.802 0-5.405 4.402-9.806
 9.806-9.806 1.467 0 2.883.319 4.2.947l.155.075.066-.155a3.767 3.767 0
 0 1 1.106-1.453l.197-.159-.225-.117A11.905 11.905 0 0 0
 12.001.001c-6.619 0-12 5.381-12 12s5.381 12 12 12 12-5.381
 12-12c0-1.73-.361-3.403-1.078-4.973zM12 6.53A5.476 5.476 0 0 0 6.53
 12 5.476 5.476 0 0 0 12 17.47 5.476 5.476 0 0 0 17.47 12 5.479 5.479
 0 0 0 12 6.53zm10.345-2.007a2.494 2.494 0 1 1-4.988 0 2.494 2.494 0 0
 1 4.988 0z" />
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

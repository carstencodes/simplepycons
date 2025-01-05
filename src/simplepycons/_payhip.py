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


class PayhipIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "payhip"

    @property
    def original_file_name(self) -> "str":
        return "payhip.svg"

    @property
    def title(self) -> "str":
        return "Payhip"

    @property
    def primary_color(self) -> "str":
        return "#5C6AC4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Payhip</title>
     <path d="M3.695 0A3.696 3.696 0 0 0 0 3.695v12.92A7.384 7.384 0 0
 0 7.385 24h12.92A3.696 3.696 0 0 0 24 20.305V0H3.695zm11.653
 5.604a3.88 3.88 0 0 1 .166 0 3.88 3.88 0 0 1 2.677 1.132 3.88 3.88 0
 0 1 0
 5.48l-.36.356c-1.826-1.825-3.648-3.656-5.476-5.482l.358-.354a3.88
 3.88 0 0 1 2.635-1.132zm-6.627.125a3.88 3.88 0 0 1 2.566 1c2.068
 2.062 4.127 4.133 6.192 6.199l-5.481 5.482-6.19-6.203C3.549 9.7 5.346
 5.702 8.722 5.729zm-1.744 1.71a.464.464 0 0 0-.465.465v1.817c0
 .256.208.463.465.463h1.816a.464.464 0 0 0
 .463-.463l.008-1.817A.464.464 0 0 0 8.8 7.44H6.977z" />
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

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


class RevolutIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "revolut"

    @property
    def original_file_name(self) -> "str":
        return "revolut.svg"

    @property
    def title(self) -> "str":
        return "Revolut"

    @property
    def primary_color(self) -> "str":
        return "#191C1F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Revolut</title>
     <path d="M20.9133 6.9566C20.9133 3.1208 17.7898 0 13.9503
 0H2.424v3.8605h10.9782c1.7376 0 3.177 1.3651 3.2087
 3.043.016.84-.2994 1.633-.8878
 2.2324-.5886.5998-1.375.9303-2.2144.9303H9.2322a.2756.2756 0 0
 0-.2755.2752v3.431c0 .0585.018.1142.052.1612L16.2646
 24h5.3114l-7.2727-10.094c3.6625-.1838 6.61-3.2612 6.61-6.9494zM6.8943
 5.9229H2.424V24h4.4704z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developer.revolut.com/docs/resources/'''

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

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


class MonzoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "monzo"

    @property
    def original_file_name(self) -> "str":
        return "monzo.svg"

    @property
    def title(self) -> "str":
        return "Monzo"

    @property
    def primary_color(self) -> "str":
        return "#14233C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Monzo</title>
     <path d="M4.244 1.174a.443.443 0 00-.271.13l-3.97
 3.97-.001.001c3.884 3.882 8.093 8.092 11.748 11.748v-8.57L4.602
 1.305a.443.443 0 00-.358-.131zm15.483 0a.443.443 0 00-.329.13L12.25
 8.456v8.568L24 5.275c-1.316-1.322-2.647-2.648-3.97-3.97a.443.443 0
 00-.301-.131zM0 5.979l.002 10.955c0 .294.118.577.326.785l4.973
 4.976c.28.282.76.083.758-.314V12.037zm23.998.003l-6.06
 6.061v10.338c-.004.399.48.6.76.314l4.974-4.976c.208-.208.326-.49.326-.785z"
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

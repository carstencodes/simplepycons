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


class MtrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mtr"

    @property
    def original_file_name(self) -> "str":
        return "mtr.svg"

    @property
    def title(self) -> "str":
        return "MTR"

    @property
    def primary_color(self) -> "str":
        return "#AC2E45"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MTR</title>
     <path d="M11.987 1.913c-1.9 0-3.693.321-5.298.883C2.756 4.268 0
 7.826 0 12c0 4.147 2.756 7.706 6.689 9.204 1.632.562 3.425.883
 5.325.883a16.74 16.74 0 0 0 5.27-.856C21.217 19.759 24 16.174 24
 12.027V12c0-4.174-2.783-7.732-6.716-9.204a16.295 16.295 0 0
 0-5.297-.883zM10.89 5.257h2.167v3.827c1.525-.402 2.702-1.766
 2.782-3.399l2.168.027c-.16 2.73-2.22 4.95-4.897 5.378v1.793c2.676.428
 4.736 2.675 4.924
 5.404l-2.167.028c-.08-1.633-1.258-2.997-2.783-3.425v3.853h-2.167V14.89a3.775
 3.775 0 0 0-2.81 3.425l-2.167-.028a5.868 5.868 0 0 1
 4.923-5.404v-1.766C8.187 10.716 6.1 8.468 5.94 5.74l2.167-.027A3.711
 3.711 0 0 0 10.89 9.11Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:MTR_('''

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

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


class SimplenoteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "simplenote"

    @property
    def original_file_name(self) -> "str":
        return "simplenote.svg"

    @property
    def title(self) -> "str":
        return "Simplenote"

    @property
    def primary_color(self) -> "str":
        return "#3361CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Simplenote</title>
     <path d="M3.466 3.62c-.004.052-.014.104-.018.158-.406 4.626 2.747
 8.548 8.03 9.994 2.024.553 5.374 2.018 5.06 5.599a5.063 5.063 0 0
 1-1.803 3.46c-1.022.857-2.308 1.21-3.64 1.166C5.147 23.794 0 18.367 0
 12.05c0-3.285 1.325-6.262 3.467-8.428zM9.82 1.032c.907-.762
 2.056-1.078 3.235-1.027C18.996.27 24 5.67 24 11.936c0 2.855-1.001
 5.478-2.667
 7.536.332-4.908-2.94-8.897-8.59-10.441-2.337-.64-4.749-2.274-4.514-4.948A4.467
 4.467 0 0 1 9.82 1.03z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://en.wikipedia.org/wiki/File:Simplenote'''

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

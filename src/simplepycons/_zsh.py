#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class ZshIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zsh"

    @property
    def original_file_name(self) -> "str":
        return "zsh.svg"

    @property
    def title(self) -> "str":
        return "Zsh"

    @property
    def primary_color(self) -> "str":
        return "#F15A24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zsh</title>
     <path d="M11.415 5.038a.58.58 0 0 0-.543.197L.135 18.021a.58.58 0
 0 0 .071.814.58.58 0 0 0 .815-.07L11.757 5.979a.58.58 0 0
 0-.07-.815.6.6 0 0 0-.272-.126m-8.113.317a3.133 3.133 0 0 0-3.12 3.12
 3.13 3.13 0 0 0 3.12 3.119A3.133 3.133 0 0 0 6.42 8.475a3.13 3.13 0 0
 0-3.119-3.119m0 1.806a1.3 1.3 0 0 1 1.314 1.313 1.3 1.3 0 0 1-1.314
 1.312A1.3 1.3 0 0 1 1.99 8.475a1.3 1.3 0 0 1 1.312-1.314m5.253
 5.253a3.13 3.13 0 0 0-3.119 3.119 3.13 3.13 0 0 0 3.12 3.118 3.133
 3.133 0 0 0 3.118-3.12 3.133 3.133 0 0 0-3.119-3.118m0 1.805a1.3 1.3
 0 0 1 1.313 1.314c0 .735-.577 1.312-1.312 1.312a1.3 1.3 0 0
 1-1.314-1.312 1.3 1.3 0 0 1 1.313-1.314m7.201 3.276a.58.58 0 0
 0-.578.578.58.58 0 0 0 .578.578h7.666a.58.58 0 0 0 .579-.578.58.58 0
 0 0-.579-.578Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Zsh-art/logo/blob/17617f2f'''

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

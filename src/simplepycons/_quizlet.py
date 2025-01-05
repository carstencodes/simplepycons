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


class QuizletIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "quizlet"

    @property
    def original_file_name(self) -> "str":
        return "quizlet.svg"

    @property
    def title(self) -> "str":
        return "Quizlet"

    @property
    def primary_color(self) -> "str":
        return "#4255FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Quizlet</title>
     <path d="M12.779.025a11.789 11.789 0 0 0-5.338.896A11.829 11.829
 0 0 0 3.058 4.11 11.928 11.928 0 0 0 .427 14.363a11.92 11.92 0 0 0
 2.3 4.921 11.842 11.842 0 0 0 4.24 3.378 11.783 11.783 0 0 0
 10.533-.226.327.327 0 0 1 .331.018 9.136 9.136 0 0 0 5.197
 1.545.332.332 0 0 0 .332-.332v-4.038a.334.334 0 0 0-.276-.331 4.732
 4.732 0 0 1-1.106-.319.329.329 0 0 1-.191-.352.33.33 0 0 1 .05-.133
 11.943 11.943 0 0 0 .772-11.871 11.87 11.87 0 0 0-4.042-4.628A11.793
 11.793 0 0 0 12.765.018l.013.007h.001ZM4.843 11.898a7.24 7.24 0 0 1
 1.205-4.005 7.18 7.18 0 0 1 3.215-2.657 7.133 7.133 0 0 1 7.815 1.558
 7.239 7.239 0 0 1 1.555 7.854 7.202 7.202 0 0 1-2.643 3.234 7.147
 7.147 0 0 1-9.049-.896 7.228 7.228 0 0 1-2.103-5.089l.005.001Z" />
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

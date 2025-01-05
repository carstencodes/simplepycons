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


class GradlePlayPublisherIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gradleplaypublisher"

    @property
    def original_file_name(self) -> "str":
        return "gradleplaypublisher.svg"

    @property
    def title(self) -> "str":
        return "Gradle Play Publisher"

    @property
    def primary_color(self) -> "str":
        return "#82B816"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gradle Play Publisher</title>
     <path d="M9.191 6.777a1.409 1.409 0 0 0-1.384 1.41v7.62a1.406
 1.406 0 0 0 2.109 1.218l6.633-3.832a1.38 1.38 0 0 0 0-2.392L9.916
 6.969a1.39 1.39 0 0 0-.725-.192zm.381 1.33a.895.895 0 0 1
 .602.106l5.22 3.014a.896.896 0 0 1 0 1.546l-5.22 3.014a.894.894 0 0
 1-1.342-.773V8.986a.895.895 0 0 1 .74-.878zM8.154.633C3.414 2.233 0
 6.716 0 12c0 6.626 5.374 12 12 12 5.161 0 9.568-3.266
 11.258-7.84l-3.838-.844-5.148 5.149-8.465-2.272-2.272-8.465
 5.059-5.056zM12 0c-.471 0-.929.025-1.387.076l.412 3.801 7.168 1.924
 1.91 7.101 3.774.832c.084-.567.123-1.14.123-1.734
 0-6.626-5.374-12-12-12z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Triple-T/gradle-play-publi'''

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
        yield from [
            "gpp",
            "Triple-T",
        ]

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


class AppsignalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "appsignal"

    @property
    def original_file_name(self) -> "str":
        return "appsignal.svg"

    @property
    def title(self) -> "str":
        return "AppSignal"

    @property
    def primary_color(self) -> "str":
        return "#21375A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AppSignal</title>
     <path d="M21.003 7.328c-1.781 0-3.055 1.57-4.368
 3.318-.815-3.714-1.72-7.424-4.601-7.424-2.881 0-3.789 3.71-4.617
 7.427-1.31-1.752-2.584-3.32-4.365-3.32C1.918 7.329 0 8.098 0
 10.986v5.24c0 2.832 1.512 3.527 2.42 3.766 1.565.406 5.334.786
 9.578.786s8.013-.38 9.579-.786c.907-.24 2.423-.934
 2.423-3.766v-5.24c0-2.888-1.92-3.658-3.052-3.658m-8.914-2.469c1.726 0
 2.384 3.406 3.3 7.493-1.004 1.238-2.072 2.236-3.3 2.236-1.228
 0-2.292-.998-3.3-2.236.857-3.822 1.519-7.493 3.3-7.493M1.664
 16.242v-5.24c0-1.823.981-2.02 1.414-2.02 1.257 0 2.62 2.096 3.893
 3.78-.91 3.818-1.873 6.143-4.145
 5.664-.593-.16-1.15-.537-1.15-2.167m4.46 2.655c1.006-1.093 1.638-2.8
 2.139-4.607 1.05 1.103 2.266 1.935 3.772 1.935 1.506 0 2.718-.832
 3.773-1.935.488 1.807 1.13 3.514 2.135 4.607a67.507 67.507 0 0
 1-11.806 0m16.282-2.655c0 1.637-.556 2.007-1.15
 2.167-2.275.482-3.235-1.846-4.145-5.665 1.287-1.683 2.62-3.779
 3.894-3.779.425 0 1.414.197 1.414 2.02z" />
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

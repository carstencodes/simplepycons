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


class MuralIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mural"

    @property
    def original_file_name(self) -> "str":
        return "mural.svg"

    @property
    def title(self) -> "str":
        return "Mural"

    @property
    def primary_color(self) -> "str":
        return "#FF4B4B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mural</title>
     <path d="M20.53 8.118H24v13.258h-3.47V8.118zM5.497 6.094A2.03
 2.03 0 0 1 7.524 8.12h3.47a5.503 5.503 0 0 0-5.497-5.497A5.503 5.503
 0 0 0 0 8.121h3.47a2.03 2.03 0 0 1 2.027-2.027zm2.027 15.285
 3.47-.002V8.12h-3.47v13.258zm8.952-.005v-3.468h-3.47l-2.013.001v3.47l5.483-.003zm0-13.256a2.03
 2.03 0 0 1 2.027-2.027V2.62a5.503 5.503 0 0 0-5.497
 5.497v9.788h3.47V8.118zm4.055 0H24a5.503 5.503 0 0
 0-5.497-5.497v3.47a2.03 2.03 0 0 1 2.027 2.027zM0
 21.378h3.47V8.122H0V21.38z" />
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

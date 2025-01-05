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


class SonosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sonos"

    @property
    def original_file_name(self) -> "str":
        return "sonos.svg"

    @property
    def title(self) -> "str":
        return "Sonos"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sonos</title>
     <path d="M12.988 12.36l-2.813-2.634v4.429h.837V11.7l2.813
 2.633V9.905h-.837zM6.464 9.665A2.3 2.3 0 0 0 4.13 12c0 1.257 1.077
 2.334 2.334 2.334A2.3 2.3 0 0 0 8.798 12a2.3 2.3 0 0 0-2.334-2.334m0
 3.83A1.482 1.482 0 0 1 4.968 12c0-.838.658-1.496 1.496-1.496S7.96
 11.162 7.96 12s-.658 1.496-1.496 1.496M2.694
 12c-.24-.18-.54-.3-.958-.419-.838-.24-.838-.479-.838-.598
 0-.24.299-.48.718-.48.36 0
 .658.18.778.24l.06.06.658-.479-.06-.06s-.538-.598-1.436-.598c-.419
 0-.838.12-1.137.359-.3.24-.479.598-.479.958s.18.718.479.957c.24.18.538.3.957.42.838.239.838.478.838.598
 0 .239-.299.478-.718.478-.359
 0-.658-.18-.778-.239l-.06-.06-.658.479.06.06s.538.598 1.436.598c.42 0
 .838-.12 1.137-.359.3-.24.48-.598.48-.957
 0-.36-.18-.659-.48-.958m14.843-2.334A2.3 2.3 0 0 0 15.202 12a2.337
 2.337 0 0 0 2.334 2.334A2.3 2.3 0 0 0 19.87 12a2.337 2.337 0 0
 0-2.334-2.334m0 3.83A1.482 1.482 0 0 1 16.04 12c0-.838.658-1.496
 1.496-1.496s1.496.658 1.496 1.496-.718 1.496-1.496
 1.496m3.77-1.556c.24.18.54.3.958.42.838.239.838.478.838.598 0
 .239-.299.478-.718.478-.36
 0-.658-.18-.778-.239h-.06l-.658.479.06.06s.538.598 1.436.598c.419 0
 .838-.12
 1.137-.359s.479-.598.479-.958-.18-.718-.479-.957c-.24-.18-.538-.3-.957-.42-.838-.239-.838-.478-.838-.598
 0-.239.299-.478.718-.478.359 0
 .658.18.778.239l.06.06.658-.479-.06-.06s-.538-.598-1.436-.598c-.42
 0-.838.12-1.137.359-.3.24-.48.598-.48.957-.059.36.12.659.48.898" />
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

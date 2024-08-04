#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class FluxusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fluxus"

    @property
    def original_file_name(self) -> "str":
        return "fluxus.svg"

    @property
    def title(self) -> "str":
        return "Fluxus"

    @property
    def primary_color(self) -> "str":
        return "#FFFFFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fluxus</title>
     <path d="M14.348 19.35a2738.241 2738.241 0 0 0-3.926-5.741 595.98
 595.98 0 0 1-1.5-2.194 433.452 433.452 0 0
 0-1.646-2.396c-.493-.712-.88-1.343-.86-1.404.021-.06.944-.73
 2.05-1.489 4.797-3.285 8.82-6.032 8.962-6.117.124-.075.152.287.147
 1.963l-.005 2.055-2.993 2.02c-1.647 1.111-2.975 2.072-2.953
 2.136.117.326 2.53 3.694 2.645 3.694.11 0 1.55-.937
 3.084-2.005.224-.156.227-.125.226
 1.905v2.063l-.692.446c-.38.245-.692.49-.692.544 0 .054.313.545.694
 1.09l.695.993-.03 3.543-.03 3.544z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/YieldingFluxus/fluxuswebsi'''

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

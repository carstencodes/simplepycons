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


class DaskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dask"

    @property
    def original_file_name(self) -> "str":
        return "dask.svg"

    @property
    def title(self) -> "str":
        return "Dask"

    @property
    def primary_color(self) -> "str":
        return "#FC6E6B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dask</title>
     <path d="m11.246 9.754 5.848-3.374a.202.202 0 0 0
 .1-.175l.002-2.553c0-.324-.133-.645-.392-.841a1 1 0 0
 0-1.118-.074l-2.425 1.4-6.436 3.712a1.007 1.007 0 0 0-.504.872l-.003
 8.721v2.825c0 .324.132.645.39.842.335.253.766.278
 1.12.074l2.363-1.364a.202.202 0 0 0 .101-.175l.003-8.244a1.902 1.902
 0 0 1 .951-1.646Zm10.316-4.336a1.005 1.005 0 0 0-.504-.137.997.997 0
 0 0-.503.137l-8.86 5.112a1.01 1.01 0 0 0-.505.87l-.003 11.591c0
 .364.188.69.503.872a.995.995 0 0 0 1.007 0l8.86-5.112a1.01 1.01 0 0 0
 .504-.872l.004-11.59a.997.997 0 0 0-.503-.871ZM6.378
 7.074l6.334-3.655a.202.202 0 0 0
 .1-.175l.001-2.193c0-.324-.133-.646-.392-.84a1 1 0 0
 0-1.118-.075L2.443 5.25a1.007 1.007 0 0 0-.504.872l-.003 11.546c0
 .324.133.645.39.842a1 1 0 0 0 1.12.074l1.877-1.082a.202.202 0 0 0
 .1-.175l.003-8.605c0-.68.363-1.307.952-1.647z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/dask/dask/blob/67e64892251'''

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

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


class FeedlyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "feedly"

    @property
    def original_file_name(self) -> "str":
        return "feedly.svg"

    @property
    def title(self) -> "str":
        return "Feedly"

    @property
    def primary_color(self) -> "str":
        return "#2BB24C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Feedly</title>
     <path d="M13.85995 1.98852a2.60906 2.60906 0 00-3.72608 0L.76766
 11.52674a2.72906 2.72906 0 000 3.79508l6.68415 6.80816a2.61806
 2.61806 0 001.74004.66401h5.61313a2.61606 2.61606 0
 001.87204-.79101l6.55415-6.67516a2.72606 2.72606 0
 000-3.79508l-9.37021-9.54422zm-.26 17.4224l-.93502.95002a.372.372 0
 01-.268.114h-.80003a.376.376 0 01-.247-.096l-.95402-.97002a.39.39 0
 010-.54201l1.33703-1.36003a.37.37 0 01.531 0l1.33704 1.36103a.389.389
 0 010 .543zm0-5.71113l-3.73709 3.80808a.374.374 0
 01-.268.111h-.79902a.376.376 0 01-.25-.093l-.95103-.97002a.391.391 0
 010-.54401l4.1391-4.2141a.372.372 0 01.531 0l1.33704 1.36204a.386.386
 0 010 .54zm0-5.70713L7.0598 14.6528a.372.372 0
 01-.268.113h-.80002a.373.373 0 01-.24901-.094l-.95302-.97202a.388.388
 0 010-.54001L11.7329 6.0896a.372.372 0 01.531 0l1.33704
 1.36004a.389.389 0 010 .543z" />
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

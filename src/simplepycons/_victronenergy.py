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


class VictronEnergyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "victronenergy"

    @property
    def original_file_name(self) -> "str":
        return "victronenergy.svg"

    @property
    def title(self) -> "str":
        return "Victron Energy"

    @property
    def primary_color(self) -> "str":
        return "#0066B2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Victron Energy</title>
     <path d="M7.183 4.65c-.522.001-1.295.137-2.1.751 0 0-1.7
 1.039-2.096 5.166 0 0-.144 1.019-.066 1.535 0 0 .066.603.687.657 0 0
 .749.058.797-.644.047-.702.063-.987.063-.987S4.586 8.384 5.7
 6.993l.269.202s.38-1.441 1.874-2.465c0
 0-.254-.081-.66-.08Zm2.729.023c-.635.001-1.632.167-2.437 1.042 0
 0-1.279 1.14-1.656 3.973 0 0-.158 1.522-.185 2.262 0
 0-.013.718.678.809 0 0 .71.044.757-.711 0 0 .046-3.468
 1.329-5.055l.319.198s.555-1.603 1.826-2.461c0
 0-.25-.058-.631-.057Zm2.854.016c-.057-.001-.116 0-.175.003 0
 0-1.792-.073-2.844 1.733 0 0-1.216 1.771-1.211 5.397 0
 0-.074.86.601.938 0 0 .798.05.798-.862 0 0 .036-3.578 1.401-5.025 0 0
 1.209 1.452 1.308 4.866 0 0 .042 2.34.479 3.63 0 0
 .395-1.448.475-3.452 0 0-.034-.366.284-.624 0 0 .209-.102.168-.468 0
 0-.292-2.978-1.284-4.666 0 0 2.103-.136 2.52 4.071 0 0
 .004.615.345.999 0 0 .25.177.275.609 0 0 .061.595-.118 2.521 0
 0-.042.422.144 1.021 0 0 .52-1.438.382-2.848 0 0-.068-1.144.501-1.53
 0 0-.048-3.193-1.318-4.941 0
 0-.944-1.359-2.731-1.372Zm-8.559.019c-.563.005-1.316.162-2.073.771 0
 0-1.8 1.208-2.13 6.299 0 0-.1.847.648.972 0 0
 .753.145.853-.489.099-.636.08-3.847 1.503-5.495 0 0
 .138-.208.516-.371.317-.194.567-.55.753-.832 0 0 .277-.369.867-.714 0
 0-.374-.146-.937-.141ZM8.068 8.62s-.519 1.438-.383 2.847c0 0 .069
 1.145-.5 1.531 0 0 .048 3.194 1.319 4.941 0 0 1.004 1.448 2.905 1.369
 0 0 1.792.073 2.845-1.734 0 0 1.214-1.77 1.21-5.397 0 0
 .074-.859-.601-.938 0 0-.799-.05-.799.863 0 0-.035 3.578-1.401 5.024
 0 0-1.209-1.451-1.308-4.864 0 0-.041-2.34-.477-3.63 0 0-.396
 1.446-.475 3.451 0 0 .033.366-.285.624 0 0-.209.102-.169.468 0 0 .293
 2.979 1.286 4.666 0 0-2.104.136-2.521-4.071 0 0-.004-.615-.345-.999 0
 0-.25-.177-.275-.608 0 0-.061-.596.117-2.522 0 0
 .042-.422-.143-1.021Zm15.161
 2.617c-.217-.011-.66.026-.734.503-.099.634-.08 3.845-1.503 5.494 0
 0-.138.208-.517.37-.315.195-.565.551-.752.833 0 0-.278.369-.867.713 0
 0 1.495.588 3.01-.63 0 0 1.8-1.207 2.129-6.299 0 0
 .101-.847-.647-.971 0
 0-.047-.01-.119-.013Zm-5.571.004c-.137.002-.687.051-.726.711 0 0-.048
 3.468-1.331 5.056l-.318-.198s-.555 1.603-1.825 2.46c0 0 1.779.415
 3.068-.984 0 0 1.278-1.141 1.655-3.973 0 0 .158-1.522.185-2.263 0 0
 .014-.718-.677-.808l-.031-.001Zm2.701.001c-.144-.002-.723.03-.763.643l-.065.987s-.118
 2.744-1.231 4.136l-.269-.202s-.38 1.44-1.874 2.464c0 0 1.329.422
 2.76-.671 0 0 1.699-1.038 2.096-5.166 0 0 .145-1.019.065-1.535 0
 0-.064-.603-.687-.656h-.032Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.victronenergy.com/information/pre'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.victronenergy.com/information/pre'''

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